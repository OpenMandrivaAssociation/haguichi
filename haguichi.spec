# Workaround for Clang 16
%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Name:           haguichi
Version:        1.4.6
Release:        1
Summary:        Hamachi Network Manager
License:        GPLv3+
Group:          Productivity/Networking/Other
URL:            https://haguichi.net
Source0:        https://github.com/ztefn/haguichi/releases/download/%{version}/%{name}-%{version}.tar.xz
# Mirror source: https://launchpad.net/haguichi/1.4/%{version}/+download/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Haguichi provides a graphical frontend for Hamachi.
It features customizable commands, notification bubbles, tooltips, along with a
searchable, sortable and collapsible network list. It also can backup and
restore the Hamachi configuration directory.

%lang_package

%prep
%autosetup -p1

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
%{_datadir}/locale/*/LC_MESSAGES/haguichi.mo
