Summary:	KDirStat - disk usage utility
Summary(pl):	KDirStat - narzêdzie pokazuj±ce zajêto¶æ dysku
Name:		kdirstat
Version:	2.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://kdirstat.sourceforge.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	b8e368621ed11b046c30a6498e00d75e
Source1:	%{name}.png
URL:		http://kdirstat.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Graphical disk usage utility, very much like the Unix "du" command,
plus some cleanup facilities to reclaim disk space.

%description -l pl
Graficzne narzêdzie pokazuj±ce zajêto¶æ dysku, podobne do uniksowego
polecenia "du" z dodatkowymi mo¿liwo¶ciami sprz±tania w celu
zwolnienia miejsca.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kdirstat.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdirstat
%{_datadir}/apps/kdirstat
%{_desktopdir}/kdirstat.desktop
%{_pixmapsdir}/kdirstat.png
%{_pixmapsdir}/*/*/apps/*.png
