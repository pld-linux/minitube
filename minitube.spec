%define		http_version		68b9cf0
%define		idle_version		6aa092d
%define		js_version		a3630ba
%define		media_version		b2f5678
%define		promises_version	e6e5653
%define		updater_version		17b8f7b

Summary:	Minitube is a native YouTube client
Summary(hu.UTF-8):	Minitube egy natív YouTube kliens
Name:		minitube
Version:	3.9.3
Release:	1
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	https://github.com/flaviotordini/minitube/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4ed30b58656f14a9266689cc760431d5
Source1:	https://github.com/flaviotordini/http/archive/%{http_version}/http-%{http_version}.tar.gz
# Source1-md5:	f530cab88fa9425029c387f1afe05861
Source2:	https://github.com/flaviotordini/idle/archive/%{idle_version}/idle-%{idle_version}.tar.gz
# Source2-md5:	67d891738ca9f45acddbadb9c9c0204d
Source3:	https://github.com/flaviotordini/js/archive/%{js_version}/js-%{js_version}.tar.gz
# Source3-md5:	a2172ded2f75b6292f6d99e5e0e28165
Source4:	https://github.com/flaviotordini/media/archive/%{media_version}/media-%{media_version}.tar.gz
# Source4-md5:	5eedd12aad57983407ebd3086cec03fb
Source5:	https://github.com/flaviotordini/promises/archive/%{promises_version}/promises-%{promises_version}.tar.gz
# Source5-md5:	d6db801932cd123563bec343ee05bd59
Source6:	https://github.com/flaviotordini/updater/archive/%{updater_version}/updater-%{updater_version}.tar.gz
# Source6-md5:	6e531f6cfb1c64f5261f73b9728753e1
URL:		https://flavio.tordini.org/minitube
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Declarative-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	mpv-client-devel >= 0.29.0
BuildRequires:	phonon-qt5-devel
BuildRequires:	qt5-build >= 5.12
BuildRequires:	qt5-linguist >= 5.12
BuildRequires:	qt5-qmake >= 5.12
BuildRequires:	rpmbuild(macros) >= 2.016
Requires:	Qt5Sql-sqldriver-sqlite3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minitube is a native YouTube client. With it you can watch YouTube
videos in a new way: you type a keyword, Minitube gives you an endless
video stream. Minitube does not require the Flash Player.

%description -l hu.UTF-8
Minitube egy natív YouTube kliens. Ezzel egy új módon nézheted a
YouTube videókat: beírod a keresett kifejezést, és a Minitube egy
végtelen videó stream-et biztosít. A Minitube-nak nincs szüksége Flash
Player-re.

%prep
%setup -q -a1 -a2 -a3 -a4 -a5 -a6

for dir in http idle js media promises updater ; do
	%{__mv} $dir-*/* lib/$dir/
	%{__rm} -r $dir-*
done

%build
%{qmake_qt5}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

INSTALL_ROOT=$RPM_BUILD_ROOT \
	%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/*/*/apps/%{name}.*
%{_datadir}/metainfo/org.tordini.flavio.minitube.metainfo.xml
