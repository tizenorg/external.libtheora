Name:       libtheora
Summary:    Theora Video Compression Codec
Version:    1.1.1
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://www.theora.org/
Source0:    http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.bz2
Source1001: packaging/libtheora.manifest 
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(libpng)

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Theora is a free and open video compression format from the Xiph.org Foundation.
It can be used to distribute film and video online and on disc without the
licensing and royalty fees or vendor lock-in associated with other formats.

%package devel
Summary:    Development tools for Theora applications
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: Headers for Theora Video Compression Codec

%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%configure --disable-static \
    --enable-shared \
    --disable-sdltest \
    --disable-examples

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest libtheora.manifest
%{_libdir}/libtheora.so.*
%{_libdir}/libtheoradec.so.*
%{_libdir}/libtheoraenc.so.*

%files devel
%manifest libtheora.manifest
%{_includedir}/theora
%{_libdir}/*.so
%{_libdir}/pkgconfig/theora.pc
%{_libdir}/pkgconfig/theoraenc.pc
%{_libdir}/pkgconfig/theoradec.pc

