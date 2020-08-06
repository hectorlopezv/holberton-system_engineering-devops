#installing package to install puppet lint on agents
package {
  'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
