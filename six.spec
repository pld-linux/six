Summary:	Interesting HexBoard game
Summary(pl):	Ciekawa gra planszowa
Name:		six
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://six.retes.hu/download/%{name}-%{version}.tar.gz
# Source0-md5:	129da56864fc2ca8c8c949dcc2239604
Patch0:		%{name}-desktop.patch
URL:		http://six.retes.hu/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Six is a Hex playing program for KDE. Hex is a connectivity game with
simple rules and deep strategic complexity.

%description -l pl
Gra tocz±ca siê na planszy o sze¶ciok±tnych polach, polegaj±ca na
po³±czeniu ze sob± przeciwleg³ych boków.

%prep
%setup -q
%patch0 -p1

%build
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
%{_desktopdir}/*
%{_iconsdir}/*/*/*/*.png
%{_docdir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/mimelnk/application/*
