# Search Taxonomy

The discovery process intentionally avoids relying on the single term `VPS`.

## Product synonyms

Search across:

- VPS
- VDS
- vServer
- virtual server
- virtual machine
- virtual dedicated server
- root server
- cloud server
- cloud VM
- cloud instance
- compute instance
- elastic compute
- virtual compute
- IaaS
- lightweight server
- resource pool

## CPU and performance terms

Useful for database, build, and latency-sensitive workloads:

- dedicated vCPU
- dedicated CPU
- dedicated core
- guaranteed CPU
- isolated CPU
- CPU pinning
- reserved CPU
- non-shared CPU
- AMD EPYC VPS / VDS / cloud
- Ryzen VPS / VDS / cloud
- compute optimized
- high performance VM

## Storage terms

- NVMe VPS
- Gen4 NVMe
- Gen5 NVMe
- RAID10 NVMe
- Ceph NVMe
- replicated NVMe
- triple replicated NVMe
- distributed storage
- block storage
- high IOPS
- storage optimized
- storage VPS

## Networking terms

Do not search only for `VPC`. Providers use many names for the same or adjacent concepts:

- private network
- private LAN
- private VLAN
- VPC
- VXLAN
- SDN
- vRack
- vSwitch
- virtual switch
- private mesh
- VMesh
- internal network
- private subnet
- floating IP
- BGP
- free internal traffic
- unmetered private traffic

Bandwidth discovery terms:

- unmetered VPS
- unlimited traffic
- high bandwidth VPS
- 1 Gbps VPS
- 10 Gbps VPS
- 10 TB transfer
- 20 TB transfer
- network optimized

## Automation terms

- VPS API
- cloud API
- compute API
- provisioning API
- REST API VPS
- Terraform provider
- OpenTofu provider
- Pulumi provider
- cloud-init
- user data
- metadata service
- hourly billing
- pay as you go
- per-minute billing
- on-demand VM

## Kubernetes and orchestration terms

- managed Kubernetes
- Kubernetes cloud
- K3s VPS
- Kubernetes worker node
- node pool
- autoscaling node pool
- Cluster Autoscaler provider
- Cluster API provider
- Kubernetes private network
- Cilium VPS
- Calico VPS

## Platform reverse-discovery terms

Providers can also be discovered through the technology they run:

- OpenStack public cloud
- Apache CloudStack provider
- OpenNebula cloud
- Proxmox cloud
- VirtFusion provider
- Virtualizor provider
- SolusVM provider
- Ceph cloud

## Network reverse discovery

Search infrastructure membership instead of provider marketing pages:

1. Internet exchange member lists.
2. PeeringDB networks and facilities.
3. ASN / BGP databases.
4. Datacenter tenant or partner lists.
5. Follow the organization to its official site.
6. Check whether it currently sells public compute resources.

Useful concepts:

- IX connected cloud
- local peering VPS
- own ASN VPS
- carrier neutral cloud
- sovereign cloud
- regional cloud
- local cloud provider
- in-country cloud

## Local-language discovery

Translate the concepts, not only the acronym `VPS`.

Examples:

- German: `vServer`, `Root Server`, `virtueller Server`
- Turkish: `sanal sunucu`, `VDS kiralama`, `bulut sunucu`
- Russian: `виртуальный сервер`, `аренда VDS`, `облачный сервер`
- Vietnamese: `máy chủ ảo`, `thuê VPS`, `máy chủ cloud`
- Indonesian: `VPS murah`, `server virtual`, `cloud VPS`
- Portuguese: `servidor VPS`, `servidor virtual`, `servidor cloud`
- Spanish: `servidor VPS`, `servidor virtual`, `servidor cloud`
- French: `serveur VPS`, `serveur virtuel`, `serveur cloud`
- Chinese: `云服务器`, `轻量应用服务器`, `私有网络`
- Korean: `가상 서버`, `클라우드 서버`

## Price-shaped queries

Use requirement values as discovery terms:

- `8GB VPS $10`
- `8GB VPS under $15`
- `16GB VDS $20`
- `8GB NVMe 10TB`
- `16GB dedicated vCPU NVMe`

These queries are good for discovery but promotional results require renewal-price verification.
