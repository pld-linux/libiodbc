Summary:	iODBC Driver Manager
Summary(pl):	Zarz±dca sterowników iODBC
Name:		libiodbc
Version:	2.50.2
Release:	2
License:	LGPL
Group:		Libraries
Vendor:		Ke Jin
Source0:	http://www.iodbc.org/dist/%{name}-%{version}.tar.gz
URL:		http://www.iodbc.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#AutoReqProv:	no

%description
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under an LGPL license.

%description -l pl
Zarz±dca sterowników iODBC jest woln± implementacj± zarz±dcy
sterowników zgodn± z SAG CLI i ODBC, pozwalaj±c± programistom pisaæ
aplikacje zgodne z ODBC, które mog± ³±czyæ siê z ró¿nymi bazami
z wykorzystaniem w³a¶ciwych sterowników wewnêtrznych.

Zarz±dca sterowników iODBC pierwotnie zosta³ napisany przez Ke Jina,
aktualnie jest rozwijany przez OpenLink Software.

%package devel
Summary:	Header files for iODBC development
Summary(pl):	Pliki nag³ówkowe do rozwoju aplikacji na iODBC
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package contains the header files needed to develop program that
use the driver manager.

%description devel -l pl
Zarz±dca sterowników iODBC jest woln± implementacj± zarz±dcy
sterowników zgodn± z SAG CLI i ODBC, pozwalaj±c± programistom pisaæ
aplikacje zgodne z ODBC, które mog± ³±czyæ siê z ró¿nymi bazami
z wykorzystaniem w³a¶ciwych sterowników wewnêtrznych.

Ten pakiet zawiera pliki nag³ówkowe potrzebne do budowania aplikacji
korzystaj±cych z zarz±dcy sterowników iODBC.

%package static
Summary:	Static version of iODBC libraries
Summary(pl):	Statyczna wersja bibliotek iODBC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of iODBC libraries.

%description static -l pl
Statyczna wersja bibliotek iODBC.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install odbc.ini.sample $RPM_BUILD_ROOT%{_sysconfdir}/odbc.ini

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%config %verify(not md5 size mtime) %{_sysconfdir}/odbc.ini

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
