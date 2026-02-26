# Architecture Overview

## What It Does

A **leader election demo** for distributed systems. Multiple identical app instances connect to Apache ZooKeeper and coordinate to elect exactly one leader among them. When the leader dies, another instance automatically takes over — demonstrating fault-tolerant leader failover.

## Tech Stack

| Layer | Technology |
|---|---|
| Language | **Python 3.9** |
| Coordination | **Apache ZooKeeper 3.7** (via the **Kazoo** client library) |
| Infrastructure | **Docker + Docker Compose** |

The only Python dependency is `kazoo==2.10.0`.

## Main Entry Point

**`app/main.py`** — the single source file. It:
1. Reads `HOSTNAME` (as node ID) and `ZK_HOSTS` from environment variables
2. Connects to ZooKeeper using `KazooClient`
3. Joins an election on the `/election` znode via `zk.Election()`
4. Calls `election.run(become_leader)` which **blocks** until this node wins
5. The winner prints a crown message and holds leadership for 300 seconds (simulated work)

## How to Run

```bash
docker-compose up --build --scale app=3
```

This spins up ZooKeeper + 3 competing app containers. One wins the election; stopping that container triggers automatic failover to the next.

## Project Structure

```
├── docker-compose.yaml   # Defines zookeeper + app services
├── app/
│   ├── Dockerfile         # Python 3.9-slim, installs deps, runs main.py
│   ├── main.py            # Single entry point — all logic here
│   ├── requirements.in    # Source dependency (kazoo)
│   └── requirements.txt   # Pinned dependency (kazoo==2.10.0)
├── README.md
└── .gitignore
```
