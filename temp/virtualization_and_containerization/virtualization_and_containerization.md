%% Begin Waypoint %%
- [docker](./docker.md)
- [hypervisor](./hypervisor.md)
- [platform](./platform.md)
- [runtime_environment](./runtime_environment.md)

%% End Waypoint %%


This topic covers how different types of software (like hypervisors and Docker) can be used to create isolated environments (like virtual machines and containers) where applications can run.

## Hypervisor vs. Docker 

- A [hypervisor](hypervisor.md), also known as a virtual machine monitor, is `software that creates and runs virtual machines` (VMs). A hypervisor allows multiple VMs to run on a single machine.

- [Docker](docker.md) is a [platform](platform.md) that uses containerization technology `to wrap up an application with its runtime environment into a container`, which can be run on any system that supports Docker.

## VMs vs. containers

- A VM is an `emulations of a computer system`, it includes a full copy of an operating system, the application, necessary binaries, and libraries - taking up tens of GBs. VMs can also be slow to boot.

- Docker containers are lightweight because they `share the host system's kernel`, and they don't require a full operating system per application, resulting in a smaller footprint than VMs. Containers can be started almost instantly.

  
