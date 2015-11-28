// Plugin Dependenices
var gulp = require('gulp'),
    concat = require('gulp-concat'),
    minifycss = require('gulp-minify-css'),
    sass = require('gulp-sass');

// Path Variables
var scss_src = 'dannywebsite/static/dannywebsite/sass/**/*.scss',
    scss_dst = 'dannywebsite/static/dannywebsite/css/';

gulp.task('styles', function() {
    gulp.src(scss_src)
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(scss_dst));
});

gulp.task('default',function() {
    gulp.watch(scss_src,['styles']);
});