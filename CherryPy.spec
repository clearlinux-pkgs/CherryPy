#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : CherryPy
Version  : 18.6.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/f5/f0/72f632c9503f1ffd765561e0e18eba19de746bddebe615deb699c210be60/CherryPy-18.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/f0/72f632c9503f1ffd765561e0e18eba19de746bddebe615deb699c210be60/CherryPy-18.6.0.tar.gz
Summary  : Object-Oriented HTTP framework
Group    : Development/Tools
License  : BSD-3-Clause
Requires: CherryPy-bin = %{version}-%{release}
Requires: CherryPy-license = %{version}-%{release}
Requires: CherryPy-python = %{version}-%{release}
Requires: CherryPy-python3 = %{version}-%{release}
Requires: cheroot
Requires: jaraco.collections
Requires: more-itertools
Requires: portend
Requires: zc.lockfile
BuildRequires : buildreq-distutils3
BuildRequires : cheroot
BuildRequires : jaraco.collections
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
.. image:: https://img.shields.io/pypi/v/cherrypy.svg
:target: https://pypi.org/project/cherrypy

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
Provides: pypi(cherrypy)
Requires: pypi(cheroot)
Requires: pypi(jaraco.collections)
Requires: pypi(more_itertools)
Requires: pypi(portend)
Requires: pypi(zc.lockfile)

%description python3
python3 components for the CherryPy package.


%prep
%setup -q -n CherryPy-18.6.0
cd %{_builddir}/CherryPy-18.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588302803
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/CherryPy
cp %{_builddir}/CherryPy-18.6.0/LICENSE.md %{buildroot}/usr/share/package-licenses/CherryPy/1c32898f7d523268279046931009a11aa4ad95b6
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
/usr/share/package-licenses/CherryPy/1c32898f7d523268279046931009a11aa4ad95b6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
