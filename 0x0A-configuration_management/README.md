## This is learning how to use Puppet.

### Install Puppet
* `$ apt-get install -y ruby=1:2.7+1 --allow-downgrades`
* `$ apt-get install -y ruby-augeas`
* `$ apt-get install -y ruby-shadow`
* `$ apt-get install -y puppet`


### Puppet Terms
1. Puppet Master: the master server that controls configuration on the nodes
2. Puppet Agent Node: a node controlled by a Puppet Master
3. Manifest: a file that contains a set of instructions to be executed
4. Resource: a portion of code that declares an element of the system and 
	how its state should be changed. For instance, to install a package we need
	to define a package resource and ensure its state is set to “installed”
5. Module: a collection of manifests and other related files organized in a
	pre-defined way to facilitate sharing and reusing parts of a provisioning
6. Class: just like with regular programming languages, classes are used in Puppet
	to better organize the provisioning and make it easier to reuse portions of the code
7. Facts: global variables containing information about the system, like network
	interfaces and operating system
8. Services: used to trigger service status changes, like restarting or stopping a service


