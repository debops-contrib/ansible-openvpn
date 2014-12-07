## [![DebOps project](http://debops.org/images/debops-small.png)](http://debops.org) openvpn

[![Travis CI](http://img.shields.io/travis/debops/ansible-openvpn.svg?style=flat)](http://travis-ci.org/debops/ansible-openvpn) [![test-suite](http://img.shields.io/badge/test--suite-ansible--openvpn-blue.svg?style=flat)](https://github.com/debops/test-suite/tree/master/ansible-openvpn/)  [![Ansible Galaxy](http://img.shields.io/badge/galaxy-debops.openvpn-660198.svg?style=flat)](https://galaxy.ansible.com/list#/roles/1580)
### Warning, this is a BETA role

This role has been marked by the author as a beta role, which means that it
might be significantly changed in the future. Be careful while using this role
in a production environment.

***

[OpenVPN](http://openvpn.org/) is a a secure TCP/UDP tunneling daemon.

`debops.openvpn` role can be used to install and manage `OpenVPN`
configurations for multiple connections on both client- and
server-side.


### Installation

This role requires at least Ansible `v1.7.0`. To install it, run:

    ansible-galaxy install debops.openvpn

### Documentation

More information about `debops.openvpn` can be found in the
[official debops.openvpn documentation](http://docs.debops.org/en/latest/ansible/roles/debops.openvpn.html).


### Role dependencies

- `debops.ferm`
- `debops.apt_preferences`

### Are you using this as a standalone role without DebOps?

You may need to include missing roles from the [DebOps common
playbook](https://github.com/debops/debops-playbooks/blob/master/playbooks/common.yml)
into your playbook.

[Try DebOps now](https://github.com/debops/debops) for a complete solution to run your Debian-based infrastructure.


### Authors and license

`openvpn` role was written by:
- 'Hartmut Goebel' | [e-mail](mailto:'h.goebel@crazy-compilers.com) | [website](http://www.crazy-compilers.com)

License: [GPLv3](https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29)

***

This role is part of the [DebOps](http://debops.org/) project.
