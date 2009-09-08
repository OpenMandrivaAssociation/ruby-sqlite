%define rname sqlite
%define name  ruby-%{rname}
%define oname %{rname}-ruby

%define version 2.2.3
%define release %mkrel 5

Summary: Ruby interface for the SQLite database engine
Name: %name
Version: %version
Release: %release
License: BSD-like
Group: Development/Ruby
URL: http://rubyforge.org/projects/sqlite-ruby/
Source0: %{oname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel sqlite-devel
# For the tests
BuildRequires: sqlite-tools
Provides: %{oname}

%description
Ruby interface for the SQLite database engine.

%prep
%setup -q -n %{oname}-%{version}

%build
mkdir build
cp ext/extconf.rb ext/sqlite-api.c build
cp -a lib build
pushd build
ruby extconf.rb
make
popd
ruby test/tests.rb

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
make -C build DESTDIR=%buildroot install

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/%{rname}*
%{ruby_sitearchdir}/%{rname}*
%doc ChangeLog LICENSE api doc

