Summary:	Minitube is a native YouTube client
Summary(hu.UTF-8):	Minitube egy natív YouTube kliens
Name:		minitube
Version:	2.1.3
Release:	1
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	http://flavio.tordini.org/files/minitube/%{name}-%{version}.tar.gz
# Source0-md5:	b43df4358de2e170d7e22370b39bd1ec
URL:		http://flavio.tordini.org/minitube
BuildRequires:	QtCore-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	phonon-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-linguist >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	qt4-phonon-backend
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
%setup -q -n %{name}

%build
qmake-qt4 PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

INSTALL_ROOT=$RPM_BUILD_ROOT \
	%{__make} install

# req /usr/share/icons/hicolor/512x512/apps not found
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/512x512/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/*/*/apps/%{name}.*
