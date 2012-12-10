%define name driconf
%define version 0.9.1
%define release %mkrel 5

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
Requires: glxinfo
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


%changelog
* Tue Dec 06 2011 Götz Waschk <waschk@mandriva.org> 0.9.1-5mdv2012.0
+ Revision: 738102
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-4mdv2011.0
+ Revision: 610280
- rebuild

* Wed Feb 03 2010 Thierry Vignaud <tv@mandriva.org> 0.9.1-3mdv2010.1
+ Revision: 499981
- requires glxinfo instead of mesa-demos

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-2mdv2009.0
+ Revision: 266577
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.9.1-1mdv2009.0
+ Revision: 140722
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 15 2007 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdv2008.0
+ Revision: 26895
- fix upstream menu
- drop legacy menu
- Import driconf



* Tue May 15 2007 G�tz Waschk <waschk@mandriva.org> 0.9.1-1mdv2008.0
- fix URL
- new version

* Wed Aug  2 2006 G�tz Waschk <waschk@mandriva.org> 0.9.0-4mdv2007.0
- xdg menu

* Sun May 28 2006 G�tz Waschk <waschk@mandriva.org> 0.9.0-3mdv2007.0
- fix menu and use glinfo instead of glxinfo

* Sun May 28 2006 G�tz Waschk <waschk@mandriva.org> 0.9.0-2mdv2007.0
- fix deps

* Mon Jan 30 2006 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdk
- New release 0.9.0
- use mkrel

* Fri Sep  2 2005 G�tz Waschk <waschk@mandriva.org> 0.2.7-1mdk
- update file list
- New release 0.2.7

* Mon Dec  6 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.2.2-1mdk
- initial package
