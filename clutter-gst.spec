Summary:	Library integrating clutter with GStreamer
Summary(pl.UTF-8):	Biblioteka integrująca clutter z GStreamerem
Name:		clutter-gst
Version:	2.0.6
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/clutter-gst/2.0/%{name}-%{version}.tar.xz
# Source0-md5:	35f67cfc75c4aa545db0f8b0a1f0e7a0
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	clutter-devel >= 1.6.0
BuildRequires:	cogl-devel >= 1.10.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel >= 0.6.8
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	clutter >= 1.6.0
Requires:	cogl >= 1.10.0
Requires:	glib2 >= 1:2.28.0
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library integrating clutter with GStreamer.

%description -l pl.UTF-8
Biblioteka integrująca clutter z GStreamerem.

%package devel
Summary:	Header files for clutter-gst library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clutter-gst
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 1.6.0
Requires:	cogl-devel >= 1.10.0
Requires:	glib2-devel >= 1:2.28.0
Requires:	gstreamer-devel >= 1.0.0
Requires:	gstreamer-plugins-base-devel >= 1.0.0

%description devel
Header files for clutter-gst library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter-gst.

%package static
Summary:	Static clutter-gst library
Summary(pl.UTF-8):	Statyczna biblioteka clutter-gst
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static clutter-gst library.

%description static -l pl.UTF-8
Statyczna biblioteka clutter-gst.

%package apidocs
Summary:	clutter-gst API documentation
Summary(pl.UTF-8):	Dokumentacja API clutter-gst
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
clutter-gst API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API clutter-gst.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libclutter-gst-2.0.la \
        $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstclutter.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libclutter-gst-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-gst-2.0.so.0
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstclutter.so
%{_libdir}/girepository-1.0/ClutterGst-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gst-2.0.so
%{_includedir}/clutter-gst-2.0
%{_datadir}/gir-1.0/ClutterGst-2.0.gir
%{_pkgconfigdir}/clutter-gst-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-gst-2.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
