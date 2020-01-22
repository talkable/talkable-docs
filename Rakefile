# frozen_string_literal: true
require 'mkmf'
require 'open3'

SPHINX_BUILD = ENV['SPHINX_BUILD'] || 'sphinx-build'
SOURCE_DIR   = 'source'
BUILD_DIR    = 'build'
SPHINX_OPTS  = "-b html -d #{BUILD_DIR}/doctrees #{SOURCE_DIR} #{BUILD_DIR}/html"

task :default => :help
task :help do
  system 'rake --tasks'
end

desc 'Set up deploys'
task :setup do
  sh 'git remote add staging git@github.com:talkable/void-talkable-docs.git'
end

task :environment do
  ENV['LANG'] = ENV['LC_ALL'] = 'en_US.UTF-8'
  find_executable(SPHINX_BUILD) || abort("The '#{SPHINX_BUILD}' command was not found. Make sure you have Sphinx installed, then set the SPHINX_BUILD environment variable to point to the full path of the '#{SPHINX_BUILD}' executable. Alternatively you can add the directory with the executable to your PATH. If you do not have Sphinx installed, grab it from http://sphinx-doc.org/")

  regexp = /(\d+\.)?(\d+\.)?(\*|\d+)/
  required = File.read('requirements.txt').match(regexp).to_s
  installed = Open3.capture3("#{SPHINX_BUILD} --version")[1].match(regexp).to_s
  if !required.empty? && !installed.empty? && Gem::Version.new(required) > Gem::Version.new(installed)
    abort "\nYou are running an outdated version of Sphinx #{installed}. Required version is #{required}. Run `pip3 install -r requirements.txt` to upgrade Sphinx."
  end
end

desc 'Run build in test mode'
task :test => :environment do
  sh "#{SPHINX_BUILD} -nW #{SPHINX_OPTS}"
end

task :build => :environment do
  sh "#{SPHINX_BUILD} #{SPHINX_OPTS}"

  Rake::FileList["#{BUILD_DIR}/html/**/*.html"].each do |filename|
    File.open(filename, "r+") do |file|
      old_content = file.read
      new_content = old_content.gsub(%r{<a(.*)?href="(https?://(?!(?:www\.)?talkable\.com).*?)"}, '<a \1 rel="nofollow" href="\2"')
      file.tap(&:rewind).write(new_content) if old_content != new_content
    end
  end

  puts "\nBuild finished. The HTML pages are in #{File.expand_path("#{BUILD_DIR}/html")}."
end

task :clean do
  sh "rm -rf #{BUILD_DIR}/*"
end

desc 'Make standalone HTML files'
task :preview => [:clean, :build]

desc 'Run the server on localhost:5000 and open a browser'
task :server => :preview do
  sh '(sleep 2 && open "http://localhost:5000")&'
  sh 'bundle exec foreman start'
end

desc 'Commit and deploy changes to http://docs.talkable.com'
task :deploy => :'deploy:production'

namespace :deploy do
  def deploy(domain:, html_branch:, source_branch:, disallow_robots:, push_command:)
    sh "git checkout #{html_branch}"
    sh 'git pull'
    sh "find . -not -path './.git' -not -path './.git/*' -not -path './Rakefile' -not -path './.circleci' -not -path './.circleci/*' -delete"
    sh "git checkout #{source_branch} #{SOURCE_DIR} .gitignore requirements.txt"
    sh 'git reset HEAD'
    Rake::Task[:build].invoke
    sh "(cd #{BUILD_DIR}/html && tar c ./) | (cd ./ && tar xf -)"
    sh "rm -rf #{BUILD_DIR} #{SOURCE_DIR} .buildinfo"
    File.write('.nojekyll', '')
    File.write('CNAME', domain)
    File.write('robots.txt', "User-agent: *\nDisallow: /") if disallow_robots
    sh 'git add -A'
    sh "git commit -m \"Generated gh-pages for `git log #{source_branch} -1 --pretty=short --abbrev-commit`\" && #{push_command} ; git checkout #{source_branch}"

    puts "\nDeployment finished. Check updated docs at http://#{domain}"
  end

  task :production do
    deploy(
      domain: 'docs.talkable.com',
      html_branch: 'gh-pages',
      source_branch: 'master',
      disallow_robots: false,
      push_command: 'git push origin gh-pages'
    )
  end

  desc 'Commit and deploy changes to http://void-docs.talkable.com'
  task :staging do
    deploy(
      domain: 'void-docs.talkable.com',
      html_branch: 'void-gh-pages',
      source_branch: 'void',
      disallow_robots: true,
      push_command: 'git push -f origin void-gh-pages && git push -f staging void-gh-pages:gh-pages'
    )
  end
end
