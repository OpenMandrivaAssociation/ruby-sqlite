%define rname sqlite
%define name  ruby-%{rname}
%define oname %{rname}-ruby

%define version 2.2.3
%define release %mkrel 1

Summary: Ruby interface for the SQLite database engine
Name: %name
Version: %version
Release: %release
License: BSD-like
Group: Development/Other
URL: http://rubyforge.org/projects/sqlite-ruby/
Source0: %{oname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel sqlite-devel
# For the tests
BuildRequires: sqlite-tools
Provides: %{oname}

%{expand:%%define ruby_libdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")}
%{expand:%%define ruby_archdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

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
%{ruby_libdir}/%{rname}*
%{ruby_archdir}/%{rname}*
%doc ChangeLog LICENSE api doc

