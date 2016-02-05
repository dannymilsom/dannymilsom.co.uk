// Core dependencies
var gulp = require('gulp'),
    path = require('path');

// Gulp plugin dependencies
var concat = require('gulp-concat'),
    minifycss = require('gulp-minify-css'),
    sass = require('gulp-sass');

// Base static directories
var static_dir = path.join('src', 'dannywebsite', 'static', 'dannywebsite'),
    css_dir = path.join(static_dir, 'css');
    js_dir = path.join(static_dir, 'js');

// SASS paths
var scss_src = path.join(static_dir, 'sass/**/*.scss'),
    scss_dst = path.join(static_dir, 'css');

// Compile SASS to CSS
gulp.task('styles', function() {
    gulp.src(scss_src)
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(scss_dst));
});

// Styles sources
var styles_src = [
    path.join(css_dir, 'vendor', 'bootstrap.min.css'),
    path.join(css_dir, 'layout.css'),
    path.join(css_dir, 'main.css'),
]

// Concat styles
gulp.task('concat-styles', function() {
    gulp.src(styles_src)
    .pipe(concat({ path: 'dannymilsom.css'}))
    .pipe(gulp.dest(css_dir));
});

// Script soruce paths
var scripts_src = [
    path.join(js_dir, 'vendor', 'jquery.min.js'),
    path.join(js_dir, 'vendor', 'jquery-migrate-1.0.0.min.js'),
    path.join(js_dir, 'vendor', 'underscore-min.js'),
    path.join(js_dir, 'vendor', 'backbone-min.js'),
    path.join(js_dir, 'vendor', 'bootstrap.min.js'),
    path.join(js_dir, 'vendor', 'matchMedia.js'),
    path.join(js_dir, 'layout.js'),
]

// Concat scripts
gulp.task('concat', function() {
    gulp.src(scripts_src)
    .pipe(concat({ path: 'dannymilsom.js'}))
    .pipe(gulp.dest(js_dir));
});

gulp.task('default',function() {
    gulp.watch(scss_src,['styles']);
});

gulp.task('build', ['styles', 'concat', 'concat-styles'])
