#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : enum34
Version  : 1.1.6
Release  : 42
URL      : http://pypi.debian.net/enum34/enum34-1.1.6.tar.gz
Source0  : http://pypi.debian.net/enum34/enum34-1.1.6.tar.gz
Summary  : Python 3.4 Enum backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4
Group    : Development/Tools
License  : BSD-3-Clause
Requires: enum34-license
Requires: enum34-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
========================================
        
        An enumeration is a set of symbolic names (members) bound to unique, constant
        values.  Within an enumeration, the members can be compared by identity, and
        the enumeration itself can be iterated over.
        
            from enum import Enum

%package legacypython
Summary: legacypython components for the enum34 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the enum34 package.


%package license
Summary: license components for the enum34 package.
Group: Default

%description license
license components for the enum34 package.


%package python
Summary: python components for the enum34 package.
Group: Default

%description python
python components for the enum34 package.


%prep
%setup -q -n enum34-1.1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529016881
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/enum34
cp enum/LICENSE %{buildroot}/usr/share/doc/enum34/enum_LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/enum34/enum_LICENSE

%files python
%defattr(-,root,root,-)
