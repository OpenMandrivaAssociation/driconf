%define name driconf
%define version 0.9.1
%define release %mkrel 1

Summary: DRI Configuration GUI
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://people.freedesktop.org/~fxkuehl/driconf/%{name}-%{version}.tar.bz2
Source1: %name.jpg
Patch: driconf-0.9.0-glinfo.patch
License: GPL
Group: System/Configuration/Hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: ImageMagick
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
%build
python setup.py build 

%install
rm -rf %buildroot %name.lang
python setup.py install --root=$RPM_BUILD_ROOT --prefix=%_prefix --install-purelib=%_datadir/%name
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%name
?package(%name):\
needs="x11"\
section="System/Configuration/Hardware"\
title="DriConf"\
longtitle="Configure the DRI hardware accelleration"\
icon="%name.png"\
command="%name" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=DriConf
Comment=Configure the DRI hardware accelleration
Exec=%{name}
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-System-Configuration-Hardware;Settings;HardwareSettings;
EOF


mkdir -p %buildroot{%_liconsdir,%_miconsdir}
convert -scale 48 %SOURCE1 %buildroot%_liconsdir/%name.png
convert -scale 32 %SOURCE1 %buildroot%_iconsdir/%name.png
convert -scale 16 %SOURCE1 %buildroot%_miconsdir/%name.png

%find_lang %name
#fix paths
perl -pi -e "s^/usr/local/lib/driconf^%_datadir/%name^" %buildroot%_bindir/%name
%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%postun
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root)
%doc README
%_bindir/%name
%_datadir/applications/mandriva*
%_menudir/%name
%_datadir/%name
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png
