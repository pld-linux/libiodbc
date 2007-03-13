# TODO:
#	Installed (but unpackaged) file(s) found:
#	   /usr/bin/iodbctest
#	   /usr/bin/iodbctestw
#	   /usr/share/libiodbc/samples/Makefile
#	   /usr/share/libiodbc/samples/iodbctest.c
#	   /usr/share/man/man1/iodbctest.1.gz
#	   /usr/share/man/man1/iodbctestw.1
#
# Conditional build:
%bcond_without	gtk		# don't build iodbcadm and GUI elements in drvproxy
#
Summary:	iODBC Driver Manager
Summary(pl.UTF-8):	Zarządca sterowników iODBC
Name:		libiodbc
Version:	3.52.5
Release:	0.1
License:	LGPL or BSD
Group:		Libraries
Source0:	http://www.iodbc.org/downloads/iODBC/%{name}-%{version}.tar.gz
# Source0-md5:	550234c4f9fbaf45e6e5d74c460dff0d
URL:		http://www.iodbc.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under an LGPL license.

%description -l pl.UTF-8
Zarządca sterowników iODBC jest wolną implementacją zarządcy
sterowników zgodną z SAG CLI i ODBC, pozwalającą programistom pisać
aplikacje zgodne z ODBC, które mogą łączyć się z różnymi bazami
z wykorzystaniem właściwych sterowników wewnętrznych.

Zarządca sterowników iODBC pierwotnie został napisany przez Ke Jina,
aktualnie jest rozwijany przez OpenLink Software.

%package devel
Summary:	Header files for iODBC development
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwoju aplikacji na iODBC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package contains the header files needed to develop program that
use the driver manager.

%description devel -l pl.UTF-8
Zarządca sterowników iODBC jest wolną implementacją zarządcy
sterowników zgodną z SAG CLI i ODBC, pozwalającą programistom pisać
aplikacje zgodne z ODBC, które mogą łączyć się z różnymi bazami
z wykorzystaniem właściwych sterowników wewnętrznych.

Ten pakiet zawiera pliki nagłówkowe potrzebne do budowania aplikacji
korzystających z zarządcy sterowników iODBC.

%package static
Summary:	Static version of iODBC libraries
Summary(pl.UTF-8):	Statyczna wersja bibliotek iODBC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of iODBC libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek iODBC.

%package gtk
Summary:	GTK+-based GUI for iODBC administration
Summary(pl.UTF-8):	Oparty o GTK+ interfejs do administrowania iODBC
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK+-based GUI for iODBC administration.

%description gtk -l pl.UTF-8
Oparty o GTK+ graficzny interfejs do administrowania iODBC.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	%{!?with_gtk:--disable-gui}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install etc/odbc.ini.sample $RPM_BUILD_ROOT%{_sysconfdir}/odbc.ini

# dlopened by lib*.so
rm -f $RPM_BUILD_ROOT%{_libdir}/lib{iodbcadm,drvproxy}.{a,la}
# build process side-effects
rm -f $RPM_BUILD_ROOT%{_libdir}/lib{iodbcadm,drvproxy}-gtk.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE LICENSE.BSD NEWS README
%attr(755,root,root) %{_libdir}/libiodbc.so.*.*.*
%attr(755,root,root) %{_libdir}/libiodbcinst.so.*.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/odbc.ini

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iodbc-config
%attr(755,root,root) %{_libdir}/libiodbc.so
%attr(755,root,root) %{_libdir}/libiodbcinst.so
%{_libdir}/libiodbc.la
%{_libdir}/libiodbcinst.la
%{_includedir}/*.h
%{_pkgconfigdir}/libiodbc.pc
%doc %{_mandir}/man1/iodbc-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libiodbc.a
%{_libdir}/libiodbcinst.a

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iodbcadm-gtk
%attr(755,root,root) %{_libdir}/libiodbcadm.so.*.*.*
%attr(755,root,root) %{_libdir}/libdrvproxy.so.*.*.*
%attr(755,root,root) %{_libdir}/libiodbcadm.so
%attr(755,root,root) %{_libdir}/libdrvproxy.so
%doc %{_mandir}/man1/iodbcadm-gtk.1*
%endif
