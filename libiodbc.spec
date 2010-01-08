#
# Conditional build:
%bcond_without	gtk		# don't build iodbcadm and GUI elements in drvproxy
#
Summary:	iODBC Driver Manager
Summary(pl.UTF-8):	Zarządca sterowników iODBC
Name:		libiodbc
Version:	3.52.7
Release:	2
License:	LGPL v2 or BSD
Group:		Libraries
Source0:	http://www.iodbc.org/downloads/iODBC/%{name}-%{version}.tar.gz
# Source0-md5:	ddbd274cb31d65be6a78da58fc09079a
Patch0:		%{name}-make-jN.patch
Patch1:		%{name}-build.patch
URL:		http://www.iodbc.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.4p5
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Conflicts:	unixODBC
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
Conflicts:	unixODBC-devel

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
Conflicts:	unixODBC-static

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
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I admin
%{__automake}
%{__autoheader}
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
rm -rf $RPM_BUILD_ROOT/usr/share/libiodbc/samples/

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/odbc.ini
%attr(755,root,root) %{_bindir}/iodbctest
%attr(755,root,root) %{_bindir}/iodbctestw
%attr(755,root,root) %{_libdir}/libiodbc.so.2.*.*
%attr(755,root,root) %ghost %{_libdir}/libiodbc.so.2
%attr(755,root,root) %{_libdir}/libiodbcinst.so.2.*.*
%attr(755,root,root) %ghost %{_libdir}/libiodbcinst.so.2
%{_mandir}/man1/iodbctest.1*
%{_mandir}/man1/iodbctestw.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iodbc-config
%attr(755,root,root) %{_libdir}/libiodbc.so
%attr(755,root,root) %{_libdir}/libiodbcinst.so
%{_libdir}/libiodbc.la
%{_libdir}/libiodbcinst.la
%{_includedir}/*.h
%{_pkgconfigdir}/libiodbc.pc
%{_mandir}/man1/iodbc-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libiodbc.a
%{_libdir}/libiodbcinst.a

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iodbcadm-gtk
%attr(755,root,root) %{_libdir}/libiodbcadm.so.2.*.*
%attr(755,root,root) %ghost %{_libdir}/libiodbcadm.so.2
%attr(755,root,root) %{_libdir}/libdrvproxy.so.2.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrvproxy.so.2
%attr(755,root,root) %{_libdir}/libiodbcadm.so
%attr(755,root,root) %{_libdir}/libdrvproxy.so
%{_mandir}/man1/iodbcadm-gtk.1*
%endif
