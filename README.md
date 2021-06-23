# SortedMagnitudeList
Small program that finds the magnitude of Gridcoin users from the last superblock in order from smallest to largest. Outputs a list of tuples with CPIDs as the first item and magnitudes as their second.

# Setup

Make sure you have the Gridcoin wallet installed and synced. Make sure to allow RPC connections through adding the following to your config file:

```
server=1
rpcallowip=127.0.0.1
rpcuser=<A Username for RPC>
rpcpassword=<A GOOD Password for RPC>
```

Make sure to replace the things in `<>` with actual values. Use those usernames and password you gave in the config file when the program asks for your RPC username and RPC password


# Truncated Example Output

```
[   ('058dff869037d7cd8a27e38a3239ef5e', 0.01),
    ('0e8f88f0e8109cdce2b348c07226513c', 0.01),
    ('1a602784bb4aeb1ad7910feed1e9a374', 0.01),
    ('254db9f7dae8efeab67b3e1ac7f9bc28', 0.01),
    ('43cc6d22950614e3d7f2873c2acd4fd0', 0.01),
    ('476ead9925a64941458e9892349c4cd1', 0.01),
    ('5d430084c7535d81067bfafb9be0a20e', 0.01),
    ('6218d377fda05f4251c794efc7899a92', 0.01),
```

...

```
    ('326bb50c0dd0ba9d46e15fae3484af35', 2393),
    ('e7f90818e3e87c0bbefe83ad3cfe27e1', 4919),
    ('a914eba952be5dfcf73d926b508fd5fa', 5385),
    ('66b4359476520659b8db798e6d933131', 6126),
    ('42cada039fcfb2ffe76176473a671374', 7131),
    ('14c2130aabb4176a0d3351cd136bbaa4', 7569),
    ('163f049997e8a2dee054d69a7720bf05', 8333),
    ('7d0d73fe026d66fd4ab8d5d8da32a611', 11442)]
```
