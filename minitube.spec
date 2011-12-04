Summary:	Minitube is a native YouTube client
Summary(hu.UTF-8):	Minitube egy natív YouTube kliens
Name:		minitube
Version:	1.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://flavio.tordini.org/files/minitube/%{name}-%{version}.tar.gz
# Source0-md5:	dae6a1e4d17c778d87f8683bb1774d61
Patch0:		%{name}-desktop.patch
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
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/*/*/apps/%{name}.*
