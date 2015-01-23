#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : enum34
Version  : 1.0.4
Release  : 11
URL      : https://pypi.python.org/packages/source/e/enum34/enum34-1.0.4.tar.gz
Source0  : https://pypi.python.org/packages/source/e/enum34/enum34-1.0.4.tar.gz
Summary  : Python 3.4 Enum backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4
Group    : Development/Tools
License  : BSD-3-Clause
Requires: enum34-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
enum34 is the new Python stdlib enum module available in Python 3.4
backported for previous versions of Python from 2.4 to 3.3.

%package python
Summary: python components for the enum34 package.
Group: Default

%description python
python components for the enum34 package.


%prep
%setup -q -n enum34-1.0.4

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
py.test-2.7 || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
