Summary:	KDirStat - disk usage utility
Summary(pl):	KDirStat - narzędzie pokazujące zajętość dysku
Name:		kdirstat
Version:	2.2.0
Release:	1.2
License:	GPL
Group:		X11/Applications
Source0:	http://kdirstat.sourceforge.net/download/%{name}-%{version}.tgz
Source1:	%{name}.png
URL:		http://kdirstat.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

%description
Graphical disk usage utility, very much like the Unix "du" command,
plus some cleanup facilities to reclaim disk space.

%description -l pl
Graficzne narzędzie pokazujące zajętość dysku, podobne do uniksowego
polecenia "du" z dodatkowymi możliwościami sprzątania w celu
zwolnienia miejsca.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
#%{__make} -f Makefile.cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdirstat
%{_datadir}/apps/kdirstat
%{_applnkdir}/Utilities/kdirstat.desktop
%{_pixmapsdir}/kdirstat.png
%{_pixmapsdir}/*/*/apps/*.png
