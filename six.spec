Summary:	Interesting HexBoard game
Summary(pl.UTF-8):	Ciekawa gra planszowa
Name:		six
Version:	0.5.2
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://six.retes.hu/download/%{name}-%{version}.tar.gz
# Source0-md5:	129da56864fc2ca8c8c949dcc2239604
Patch0:		%{name}-desktop.patch
URL:		http://six.retes.hu/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Six is a Hex playing program for KDE. Hex is a connectivity game with
simple rules and deep strategic complexity.

%description -l pl.UTF-8
Gra tocząca się na planszy o sześciokątnych polach, polegająca na
połączeniu ze sobą przeciwległych boków.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_docdir}/%{name},%{_iconsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Games/Board/* $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_docdir}/HTML/en/%{name}/* $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_docdir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/mimelnk/application/*
