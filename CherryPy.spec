#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : CherryPy
Version  : 18.1.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/5b/86/b3c3e43788c1004f819f017e1ad119373172b2e794a4e05628fe7bda93c0/CherryPy-18.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/86/b3c3e43788c1004f819f017e1ad119373172b2e794a4e05628fe7bda93c0/CherryPy-18.1.2.tar.gz
Summary  : Object-Oriented HTTP framework
Group    : Development/Tools
License  : BSD-3-Clause
Requires: CherryPy-bin = %{version}-%{release}
Requires: CherryPy-license = %{version}-%{release}
Requires: CherryPy-python = %{version}-%{release}
Requires: CherryPy-python3 = %{version}-%{release}
Requires: cheroot
Requires: more-itertools
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
%setup -q -n CherryPy-18.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561312021
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
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
