import os
import time
from kazoo.client import KazooClient

# Get a unique ID for this node from the container's hostname
NODE_ID = os.environ.get("HOSTNAME")
ZK_HOSTS = os.environ.get("ZK_HOSTS")
ELECTION_PATH = "/election"

print(f"[{NODE_ID}] Starting up...")

zk = KazooClient(hosts=ZK_HOSTS)
zk.start()
print(f"[{NODE_ID}] Connected to Zookeeper.")

# This is Kazoo's built-in recipe for Leader Election
election = zk.Election(ELECTION_PATH, NODE_ID)

def become_leader():
  """This function is called only when this node becomes the leader."""
  print(f"\n!!!!!!!!!!!!!! [{NODE_ID}] I AM THE LEADER! 👑 !!!!!!!!!!!!!!\n")
  
  # Simulate doing leader-only work for 300 seconds
  try:
    time.sleep(300)
  except KeyboardInterrupt:
    print(f"[{NODE_ID}] Relinquishing leadership.")

  print(f"\n!!!!!!!!!!!!!! [{NODE_ID}] I am no longer the leader. !!!!!!!!!!!!!!\n")


# The run() method blocks. It will run our `become_leader` function
# only if/when this node wins the election. If the leader dies,
# another waiting node's function will be called.
print(f"[{NODE_ID}] Waiting to become the leader...")
election.run(become_leader)