# Requirements

  * You have to have Vagrant installed on your machine, see https://www.vagrantup.com/downloads.html
  * The DigitalOcean Vagrant plugin, see https://github.com/devopsgroup-io/vagrant-digitalocean
  * An environment variable `$DIGITAL_OCEAN_TOKEN` set to a token that you received from DigitalOcean, see the start of https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-api-v2
  * An SSH key registered at DigitalOcean, see https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-digitalocean-droplets


# Deploy this Example Server

Run the following command from within the directory containing the corresponding `Vagrantfile`:

```bash
$ vagrant up --provider=digital_ocean
```

This will instantiate a droplet at DigitalOcean. Be aware that from the point of its creation you are charged. This step will take a bit.


# A Bit of Vagrant

To see, which virtual machines or remote droplets are running run:

```bash
$ vagrant global-status
id       name      provider      state    directory
-------------------------------------------------------------------------------
cdb38ff  webserver digital_ocean active   /.../remote_deployment
```

To delete the remote droplet and to stop being billed for it run:


```bash
$ vagrant destroy
```

To double check that your droplet was destroyed:

```bash
$ vagrant global-status --prune
```
