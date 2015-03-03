%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif
 
%global srcname elasticsearch
 
Name: python-elasticsearch
Version: 1.5.0
Release: 2%{?dist}
Summary: Python client for Elasticsearch
 
Group: Development/Libraries
License: Apache
URL: https://github.com/elasticsearch/elasticsearch-py
Source0: %{srcname}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
 
BuildRequires: python-setuptools
Requires: python-unittest2
 
%description
Official low-level client for Elasticsearch. It's goal is to provide common
ground for all Elasticsearch-related code in Python; because of this it tries
to be opinion-free and very extendable.
 
 
%prep
%setup -q -n %{srcname}-%{version}

 
%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
 
 
%install
rm -rf %{buildroot}
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT
 
 
%clean
rm -rf %{buildroot}
 
 
%files
%defattr(-,root,root,-)
%doc
%{python2_sitelib}/%{srcname}-%{version}.dev-py*.egg-info/*
%{python2_sitelib}/%{srcname}/* 
