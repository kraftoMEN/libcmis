#
# Conditonal build:
%bcond_without	static_libs	# static library
#
Summary:	A C++ client library for the CMIS interface
Summary(pl.UTF-8):     Biblioteka klienta C++ dla inferfejsu CMIS
Name:		libcmis
Version:	0.1.0
Release:	2
License:	GPL v2+ or LGPL v2+ or MPL v1.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libcmis/%{name}-%{version}.tar.gz
# Source0-md5:	4be634617054ada5b6d1886f63160f4f
URL:		http://sourceforge.net/projects/libcmis/
BuildRequires:	boost-devel
BuildRequires:	curl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibCMIS is a C++ client library for the CMIS interface. This allows
C++ applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%description -l pl.UTF-8
LibCMIS to biblioteka klienta C++ dla interfejsu CMIS. Pozwala ona 
aplikacjom C++ na łączenie się z każdym ECM zachowującym się jako
serwer CMIS, taki jak Alfresco, Nuxeo (biorąc pod uwagę implementacje
o otwartych źródłach).

%package devel
Summary:	Development files for CMIS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CMIS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel
Requires:	libstdc++-devel

%description devel
This package contains the header files for developing applications
that use CMIS library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji opartych na
bibliotece CMIS

%package static
Summary:	Static CMIS library
Summary(pl.UTF-8):	Statyczna biblioteka CMIS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CMIS library.

%description static -l pl.UTF-8
Statyczna biblioteka CMIS.

%package tools
Summary:	Command line tool to access CMIS
Summary(pl.UTF-8):	Narzędzie wiersza poleceń dla CMIS
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
This package contains a tool for accessing CMIS from the command line.

%description tools -l pl.UTF-8
Ten pakiet zawiera narzędzie do łączenia się do CMIS z wiersza
poleceń.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static} \
	--disable-tests \
	--disable-werror

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/%{name}-0.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcmis-0.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-0.2.so
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}-0.2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcmis-0.2.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cmis-client
