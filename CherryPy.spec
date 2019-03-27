#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : CherryPy
Version  : 18.1.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/1f/de/3327bd7168be762180924085fecef2e127d128f1d6157f88cd87fdac2971/CherryPy-18.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/de/3327bd7168be762180924085fecef2e127d128f1d6157f88cd87fdac2971/CherryPy-18.1.1.tar.gz
Summary  : Object-Oriented HTTP framework
Group    : Development/Tools
License  : BSD-3-Clause
Requires: CherryPy-bin = %{version}-%{release}
Requires: CherryPy-license = %{version}-%{release}
Requires: CherryPy-python = %{version}-%{release}
Requires: CherryPy-python3 = %{version}-%{release}
Requires: cheroot
Requires: portend
Requires: zc.lockfile
BuildRequires : buildreq-distutils3
BuildRequires : cheroot
BuildRequires : more-itertools
BuildRequires : pluggy
BuildRequires : portend
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zc.lockfile

%description
CherryPy Tutorials
------------------
This is a series of tutorials explaining how to develop dynamic web
applications using CherryPy. A couple of notes:

%package bin
Summary: bin components for the CherryPy package.
Group: Binaries
Requires: CherryPy-license = %{version}-%{release}

%description bin
bin components for the CherryPy package.


%package license
Summary: license components for the CherryPy package.
Group: Default

%description license
license components for the CherryPy package.


%package python
Summary: python components for the CherryPy package.
Group: Default
Requires: CherryPy-python3 = %{version}-%{release}
Provides: cherrypy-python

%description python
python components for the CherryPy package.


%package python3
Summary: python3 components for the CherryPy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the CherryPy package.


%prep
%setup -q -n CherryPy-18.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553717279
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/CherryPy
cp LICENSE.md %{buildroot}/usr/share/package-licenses/CherryPy/LICENSE.md
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cherryd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/CherryPy/LICENSE.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
