### Chess-Sim
Chess-Sim is a simplified clone of chess-based social networking sites. It is a hobby project I completed whilst studying to 
familiarize myself with multi-threading, computer networking concepts, and distributed design. The project simulates a chess-playing user
ecosystem, with player directories managed by centralized servers that connect user-applications with one another. The project is built 
entirely with python built-ins: pygame for game display, threading and socket libraries for customisable low-level data exchange over TCP.
Simulation and testing occurs by instantiating the application process many times on the host machine, and supplanting hypothetical RPCs
between connected devices on a distributed system with IPC-based calls on the host machine. Deployment could be easily achieved by running
the player directory on a headless cloud server, and replacing hard-coded loopback addresses with the actual IP address of the runtime
device. As a hobby project, Chess-Sim does not require implementation of less trivial distributed design features, such as the pipelining
involved in displaying viewer and impression counts live, thus the system is easily scalable for increased user-base. 