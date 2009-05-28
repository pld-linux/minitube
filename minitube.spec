Summary:	Minitube is a native YouTube client
Summary(hu.UTF-8):	Minitube egy natív YouTube kliens
Name:		minitube
Version:	0.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://flavio.tordini.org/files/minitube/%{name}-src-%{version}.tar.gz
# Source0-md5:	235d4c010438d4fed3de6a4a29755658
URL:		http://flavio.tordini.org/minitube
Patch0:		%{name}-phonon.patch
BuildRequires:	QtCore-devel
BuildRequires:	phonon-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
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
%{__sed} -i 's@\":/images\/\([^"]*\)@"%{_iconsdir}/hicolor/scalable/apps/minitube/\1@' src/*.cpp

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/minitube
install build/target/* $RPM_BUILD_ROOT%{_bindir}
install images/* $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/minitube

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_iconsdir}/hicolor/scalable/apps/minitube
