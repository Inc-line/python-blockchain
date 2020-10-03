import time

from flask import Flask, jsonify, request
from pubnub.pubnub import PubNub
from pubnub.enums import PNStatusCategory, PNHeartbeatNotificationOptions 
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from pprint import pprint

from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-b6a63c8a-f851-11ea-a11c-fa009153ffbc'
pnconfig.publish_key = 'pub-c-6f41af51-60aa-4832-a186-25aa2f4e1997'
pnconfig.uuid = "SableServerUUID-PUB"
pnconfig.heartbeat_notification_options = PNHeartbeatNotificationOptions.ALL


CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK',
    'TRANSACTION': 'TRANSACTION'
}



class Listener(SubscribeCallback):
    def __init__(self, blockchain, transaction_pool):
        self.blockchain = blockchain
        self.transaction_pool = transaction_pool


    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                self.transaction_pool.clear_blockchain_transactions(
                    self.blockchain
                    )
                print(f'\n -- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')

        elif message_object.channel == CHANNELS['TRANSACTION']:
            transaction = Transaction.from_json(message_object.message)
            self.transaction_pool.set_transaction(transaction)
            print('\n -- A new transaction has been added to the transaction pool.')

class PubSub():
    """
    Handles the publish/subscribe layer of the application
    Provides comminucation between the nodes of the blockchain network.
    """
    def __init__(self, blockchain, transaction_pool):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))

    def presence(self, pubnub, event):
        print("[PRESENCE: {}]".format(event.event))
        print("uuid: {}, channel: {}".format(event.uuid, event.channel))

    def status_callback(self, result, status, event):
        if status.is_error():
            print("Error %s" % str(status.error_data.exception))
            print("Error category #%d" % status.category)
        if not event.category == PNStatusCategory.PNConnectedCategory:
            print("[STATUS: PNConnectedCategory]")
            print("connected to channels: {}".format(event.affected_channels))
        else:
            print(str(result))

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """ 
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

    def broadcast_transaction(self, transaction):
        """
        Bradcast a transaction to all nodes.
        """
        self.publish(CHANNELS['TRANSACTION'], transaction.to_json())


def main():
    pubsub = PubSub() # pylint: disable=no-value-for-parameter

    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})

if __name__ == '__main__':
    main()