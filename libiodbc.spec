Summary:	iODBC Driver Manager
Summary(pl):	Menad¿er driverów iODBC
Name:		libiodbc
Version:	2.50.2
Release:	2
License:	LGPL
Group:		Libraries
Vendor:		Ke Jin 
Source0:	http://www.iodbc.org/dist/%{name}-%{version}.tar.gz
URL:		http://www.iodbc.org/
BuildRequires:	autoconf
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
iODBC Driver Manager jest woln± implementacj± menad¿era driverów
zgodn± z SAG CLI i ODBC, pozwalaj±c± programistom pisaæ aplikacje
zgone z ODBC, które mog± ³±czyæ siê z ró¿nymi bazami u¿ywaj±c
w³±¶ciwych driverów backendowych.

iODBC Driver Manager oryginalnie zosta³ napisany przez Ke Jina,
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
iODBC Driver Manager jest woln± implementacj± menad¿era driverów
zgodn± z SAG CLI i ODBC, pozwalaj±c± programistom pisaæ aplikacje
zgone z ODBC, które mog± ³±czyæ siê z ró¿nymi bazami u¿ywaj±c
w³±¶ciwych driverów backendowych.

Ten pakiet zawiera pliki nag³ówkowe potrzebne do budowania aplikacji
korzystaj±cych z menad¿era driverów iODBC.

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
autoconf
#automake
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install odbc.ini.sample $RPM_BUILD_ROOT%{_sysconfdir}/odbc.ini

gzip -9nf AUTHORS ChangeLog NEWS README

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
%doc *.gz
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
