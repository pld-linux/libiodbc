#
# Conditional build:
%bcond_without gtk		# don't build iodbcadm and GUI elements in drvproxy
#
Summary:	iODBC Driver Manager
Summary(pl):	Zarz±dca sterowników iODBC
Name:		libiodbc
Version:	3.51.1
Release:	1
License:	LGPL or BSD
Group:		Libraries
Source0:	http://www.iodbc.org/dist/%{name}-%{version}.tar.gz
# Source0-md5:	c63b6f3d7bc459bdf791517c84402160
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
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of iODBC libraries.

%description static -l pl
Statyczna wersja bibliotek iODBC.

%package gtk
Summary:	GTK+-based GUI for iODBC administration
Summary(pl):	Oparty o GTK+ interfejs do administrowania iODBC
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK+-based GUI for iODBC administration.

%description gtk -l pl
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libiodbc.a
%{_libdir}/libiodbcinst.a

%if 0%{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iodbcadm-gtk
%attr(755,root,root) %{_libdir}/libiodbcadm.so.*.*.*
%attr(755,root,root) %{_libdir}/libdrvproxy.so.*.*.*
%attr(755,root,root) %{_libdir}/libiodbcadm.so
%attr(755,root,root) %{_libdir}/libdrvproxy.so
%endif
