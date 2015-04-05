#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-builder
Version  : 3.2.2
Release  : 4
URL      : https://rubygems.org/downloads/builder-3.2.2.gem
Source0  : https://rubygems.org/downloads/builder-3.2.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
# Project: Builder
## Goal
Provide a simple way to create XML markup and data structures.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n builder-3.2.2
gem spec %{SOURCE0} -l --ruby > rubygem-builder.gemspec

%build
gem build rubygem-builder.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
builder-3.2.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/builder-3.2.2
ruby -v -I.:lib test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/builder-3.2.2.gem
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/BlankSlate/cdesc-BlankSlate.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/BlankSlate/find_hidden_method-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/BlankSlate/hide-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/BlankSlate/reveal-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/IllegalBlockError/cdesc-IllegalBlockError.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XChar/cdesc-XChar.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/%3c%3c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/_escape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/_escape_attribute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/_indent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/_nested_structures-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/_newline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/cache_method_call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/cache_method_calls-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/cdesc-XmlBase.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/explicit_nil_handling%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/method_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/nil%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/tag%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlBase/text%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlEvents/_end_tag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlEvents/_start_tag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlEvents/cdesc-XmlEvents.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlEvents/text%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/_attr_value-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/_end_tag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/_ensure_no_block-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/_insert_attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/_special-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/_start_tag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/_text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/cdata%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/cdesc-XmlMarkup.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/comment%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/declare%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/instruct%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/XmlMarkup/target%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/cdesc-Builder.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Builder/check_for_name_collision-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Fixnum/cdesc-Fixnum.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Fixnum/xchr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Kernel/blank_slate_method_added-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Kernel/cdesc-Kernel.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Kernel/method_added-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Module/append_features-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Module/blankslate_original_append_features-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Module/cdesc-Module.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Object/blank_slate_method_added-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Object/find_hidden_method-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Object/method_added-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/String/_blankslate_as_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/String/to_xs-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Symbol/_blankslate_as_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/Symbol/cdesc-Symbol.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/doc/releases/page-builder-1_2_4_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/doc/releases/page-builder-2_0_0_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/doc/releases/page-builder-2_1_1_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/page-CHANGES.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/page-MIT-LICENSE.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/builder-3.2.2/ri/page-Rakefile.ri
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/CHANGES
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/README.md
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/doc/jamis.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/doc/releases/builder-1.2.4.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/doc/releases/builder-2.0.0.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/doc/releases/builder-2.1.1.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/lib/blankslate.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/lib/builder.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/lib/builder/blankslate.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/lib/builder/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/lib/builder/xchar.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/lib/builder/xmlbase.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/lib/builder/xmlevents.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/lib/builder/xmlmarkup.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/rakelib/publish.rake
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/rakelib/tags.rake
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/test/performance.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/test/preload.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/test/test_blankslate.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/test/test_eventbuilder.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/test/test_markupbuilder.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/test/test_method_caching.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/test/test_namecollision.rb
/usr/lib64/ruby/gems/2.2.0/gems/builder-3.2.2/test/test_xchar.rb
/usr/lib64/ruby/gems/2.2.0/specifications/builder-3.2.2.gemspec
