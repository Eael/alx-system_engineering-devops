# Install an specific version of flask using declarative approach

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
