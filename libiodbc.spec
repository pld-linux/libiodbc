Summary: 	iODBC Driver Manager
name: 		libiodbc
version: 	2.50.2
release: 	1
Group: 		Libraries
Vendor: 	Ke Jin 
Copyright: 	LGPL
URL: 		http://www.openlinksw.com/iodbc/
Source: 	libiodbc-%{PACKAGE_VERSION}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#AutoReqProv: no

%description
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is 
currently maintained by OpenLink Software under an LGPL license.

%package devel
Summary: 	header files and libraries for iODBC development
Group: 		Development/Libraries
Requires: 	%{name} = %{version}

%description devel
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package contains the header files and libraries needed to develop
program that use the driver manager.

The iODBC Driver Manager was originally created by Ke Jin and is 
currently maintained by OpenLink Software under an LGPL license.

%package static
Summary:	Static version of iODBC libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of iODBC libraries.

%prep
%setup -q

%build
#automake
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
install -m644 odbc.ini.sample $RPM_BUILD_ROOT/etc/odbc.ini

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) /usr/lib/libiodbc.so.2.0.50
%config %verify(not md5 size mtime) /etc/odbc.ini

%files devel
%defattr(644,root,root,755)
%{_includedir}/isql.h
%{_includedir}/isqlext.h
%{_includedir}/isqltypes.h
%attr(755,root,root) %{_libdir}/libiodbc.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libiodbc.a
