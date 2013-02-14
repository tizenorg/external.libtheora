Name:       libtheora
Summary:    Theora Video Compression Codec
Version:    1.1.1
Release:    4
Group:      System/Libraries
License:    BSD
URL:        http://www.theora.org/
Source0:    http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.bz2
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

%ifarch %{arm}
export CFLAGS="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -Wformat -Wformat-security  -fmessage-length=0 -march=armv7-a -mtune=cortex-a8 -mlittle-endian -mfloat-abi=softfp -D__SOFTFP__"
export CXXFLAGS="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -Wformat -Wformat-security  -fmessage-length=0 -march=armv7-a -mtune=cortex-a8 -mlittle-endian -mfloat-abi=softfp -D__SOFTFP__"
export FFLAGS="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -Wformat -Wformat-security  -fmessage-length=0 -march=armv7-a -mtune=cortex-a8 -mlittle-endian -mfloat-abi=softfp -D__SOFTFP__"
%endif
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
%{_includedir}/theora
%{_libdir}/*.so
%{_libdir}/pkgconfig/theora.pc
%{_libdir}/pkgconfig/theoraenc.pc
%{_libdir}/pkgconfig/theoradec.pc
