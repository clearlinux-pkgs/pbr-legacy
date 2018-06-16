Name     : pbr-legacy
Version  : 3.1.1
Release  : 59
URL      : https://pypi.debian.net/pbr/pbr-3.1.1.tar.gz
Source0  : https://pypi.debian.net/pbr/pbr-3.1.1.tar.gz
Summary  : Python Build Reasonableness
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pbr-legacy-bin
Requires: pbr-legacy-license
Requires: pbr-legacy-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
============

%package bin
Summary: bin components for the pbr-legacy package.
Group: Binaries
Requires: pbr-legacy-license

%description bin
bin components for the pbr-legacy package.


%package -n pbr-legacypython
Summary: legacypython components for the pbr-legacy package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pbr-legacy package.


%package license
Summary: license components for the pbr-legacy package.
Group: Default

%description license
license components for the pbr-legacy package.


%package python
Summary: python components for the pbr-legacy package.
Group: Default

%description python
python components for the pbr-legacy package.


%prep
%setup -q -n pbr-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529115780
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pbr-legacy
cp LICENSE %{buildroot}/usr/share/doc/pbr-legacy/LICENSE
cp pbr/tests/testpackage/LICENSE.txt %{buildroot}/usr/share/doc/pbr-legacy/pbr_tests_testpackage_LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/pbr

%files -n pbr-legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/pbr-legacy/LICENSE
/usr/share/doc/pbr-legacy/pbr_tests_testpackage_LICENSE.txt

%files python
%defattr(-,root,root,-)
