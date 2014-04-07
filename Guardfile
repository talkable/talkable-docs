guard 'shell' do
  watch(%r{(.*)\.rst}) do |m|
    system("sphinx-build -b html -d build/doctrees source build/html")
  end

  watch(%r{^source/_static/}) do |m|
    system("rsync -az source/_static build/html")
  end
end

guard 'livereload' do
  watch(%r{(.*)\.rst})
  watch(%r{^source/_static/})
end
