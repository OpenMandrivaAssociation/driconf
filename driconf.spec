%define name driconf
%define version 0.9.1
%define release %mkrel 2

Summary: DRI Configuration GUI
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://people.freedesktop.org/~fxkuehl/driconf/%{name}-%{version}.tar.bz2
Patch: driconf-0.9.0-glinfo.patch
Patch1: driconf-0.9.1-desktopentry.patch
License: GPL
Group: System/Configuration/Hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
Requires: gnome-python
Requires: xdriinfo
#gw for glinfo
Requires: mesa-demos
BuildArch: noarch
Url: http://dri.sourceforge.net/cgi-bin/moin.cgi/DriConf

%description
DRIConf is the first configuration GUI for DRI. It provides a
comfortable GUI for changing the OpenGL settings.

%prep
%setup -q
%patch -p1
%patch1 -p1 -b .desktopentry

%build
python setup.py build 

%install
rm -rf %buildroot %name.lang
python setup.py install --root=$RPM_BUILD_ROOT --prefix=%_prefix --install-purelib=%_datadir/%name

install -D -m 644 %name.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop
install -D -m 644 driconf-icon.png %buildroot%_datadir/icons/hicolor/24x24/apps/%name.png

%find_lang %name
#fix paths
perl -pi -e "s^/usr/local/lib/driconf^%_datadir/%name^" %buildroot%_bindir/%name
%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc README
%_bindir/%name
%_datadir/applications/*
%_datadir/%name
%_datadir/icons/hicolor/24x24/apps/%name.png
