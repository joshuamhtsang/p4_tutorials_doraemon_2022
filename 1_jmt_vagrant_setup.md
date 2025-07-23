# Vagrant and Virtual Box VM Setup

Follow the instructions in the official [README.md](./README.md)
which suggests installing vagrant and virtual box.  The basic instructions are:

[Install Vagrant](https://developer.hashicorp.com/vagrant/install)
(note you have to manually copy and execute each line for their Ubuntu 24.04 commands...)

[Install Virtualbox](https://www.virtualbox.org/wiki/Linux_Downloads)
(download *.deb file and run... at time of wiritng I installed Virtualbox 7.1)

Then in the [./vm-ubuntu-20.04/](./vm-ubuntu-20.04/) directory, run in the terminal:

~~~
$ vagrant up --provision
~~~

Update 2025-07-23: Now WAIT! It takes some time before the VM is all setup and until it is, using the username 'p4' and password 'p4' will not work!

The '--provision' flag is sometime necesssary to mount this repo's files to the following directory inside in the guest VM:

~~~
/vagrant/
~~~

If you get an error like:

~~~
==> release: Booting VM...
There was an error while executing `VBoxManage`, a CLI used by Vagrant
for controlling VirtualBox. The command and stderr is shown below.

Command: ["startvm", "75070036-35da-4f7c-8d81-12458ead236c", "--type", "gui"]

Stderr: VBoxManage: error: AMD-V is disabled in the BIOS (or by the host OS) (VERR_SVM_DISABLED)
VBoxManage: error: Details: code NS_ERROR_FAILURE (0x80004005), component ConsoleWrap, interface IConsole
~~~

Then Virtualbox requires AMD-V enables so make sure you enable it in BIOS:

~~~
[BIOS splash screen] -> [press F2] -> [MIT settings] ->
[Frequency Settings] -> [CPU Settings] -> [SVM Mode] -> Enable
~~~

A guest OS gui should appear at the end.  Login with:

~~~
User: p4
PW: p4
~~~

I like to change some things in the Vagrantfile to make code/script editing workflow better (essentially, to enable 'edit on host, run in VM'):

1. By default, Vagrant mounts the directory containing
the Vagrantfile to /vagrant/ directory inside the guest
VM.  However, P4 tutorials disable this in their
Vagrantfile.  Do the following to re-enable mounting and point to root of
this repo.  Change the line inside
'./vm-ubuntu-20.04/Vagrantfile' from:
~~~
    config.vm.synced_folder '.', '/vagrant', disabled: true
~~~
to:
~~~
    config.vm.synced_folder './..', '/vagrant', disabled: false
~~~

Inside the guest OS, if you 'cd' to:

~~~
$ cd /vagrant/
~~~

You should now see the `exercises/` directory.

2.  If you try to edit files inside the the guest OS, you get
'Permission denied'.  So do the file editing on the host machine,
and run the binaries/commands in the guest machine.
