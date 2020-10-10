%define over 1.143.0

Name:           haguichi
Version:        1.4.3
Release:        1
Summary:        Hamachi Network Manager
License:        GPLv3+
Group:          Productivity/Networking/Other
URL:            https://www.haguichi.net/
Source0:        https://github.com/ztefn/haguichi/archive/%{over}/%{name}-%{over}.tar.gz
# Mirror source: https://launchpad.net/haguichi/s
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)

%description
Haguichi provides a graphical frontend for Hamachi.
It features customizable commands, notification bubbles, tooltips, along with a
searchable, sortable and collapsible network list. It also can backup and
restore the Hamachi configuration directory.

%lang_package

%prep
%setup -qn %{name}-%{over}

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}/%{_datadir}
%find_lang %{name}

%files
%license LICENSE
%doc AUTHORS
%{_bindir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/com.github.ztefn.haguichi.appdata.xml
%{_datadir}/applications/com.github.ztefn.haguichi.desktop
%{_datadir}/glib-2.0/schemas/com.github.ztefn.haguichi.gschema.xml
%{_datadir}/icons/hicolor/*/*/*%{name}*
#{_sysconfdir}/xdg/autostart/com.github.ztefn.haguichi.autostart.desktop
%{_datadir}/locale/*/LC_MESSAGES/haguichi.mo
