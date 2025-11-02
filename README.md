# Leader Election Demo

## What is Leader Election?

Leader election is a fundamental pattern in distributed systems where multiple nodes (servers/processes) coordinate to elect a single leader among themselves. The leader is responsible for performing critical tasks that should only be done by one node at a time, such as:

- **Coordinating distributed operations** - Making decisions that affect the entire cluster
- **Managing shared resources** - Ensuring only one node writes to a database or file
- **Task scheduling** - Distributing work to other nodes in the cluster
- **Maintaining consistency** - Preventing conflicts in distributed state

### Why is it Important?

In distributed systems, you often have multiple instances of an application running for high availability and scalability. However, certain operations must be performed by exactly one instance to avoid:

- **Data corruption** - Multiple nodes writing conflicting data
- **Duplicate work** - The same task being executed multiple times
- **Race conditions** - Conflicting operations happening simultaneously


## About This Demo Project

This is a simple demonstration of leader election using **Python**, **Apache ZooKeeper**, and **Docker**. The project shows how multiple application instances can coordinate to elect a leader, and how the system automatically recovers when the leader fails.

### Technology Stack

- **Python 3.9+** - Application runtime
- **Kazoo** - Python client library for ZooKeeper
- **Apache ZooKeeper 3.7** - Distributed coordination service
- **Docker & Docker Compose** - Containerization and orchestration

### How It Works

1. **ZooKeeper** runs as a centralized coordination service
2. **Multiple app instances** connect to ZooKeeper and participate in the election
3. **One instance becomes the leader** and performs "leader work" (simulated with a 300-second sleep)
4. **Other instances wait** for their turn to become leader
5. **If the leader dies**, the next instance automatically takes over

## Steps to Run the Demo

### Step 1: Start Services and scale up Multiple Instances

Open a **new terminal** and scale the application to multiple instances:

```bash
docker-compose up --build --scale app=3
```

This starts 3 instances of the application. You'll see:
- One instance becomes the leader (👑)
- The other two instances wait for their turn

### Step 2: Test Leader Failover

To see automatic leader election in action:

1. **Find the leader container** - Look for the container with "I AM THE LEADER! 👑" in the logs

2. **Stop the leader container**:
   ```bash
   docker ps  # Find the container ID of the leader
   docker stop <leader-container-id>
   ```

3. **Watch the logs** - You'll see one of the waiting instances automatically become the new leader!

### Step 3: Stop the Demo

To stop all containers:

```bash
docker-compose down
```