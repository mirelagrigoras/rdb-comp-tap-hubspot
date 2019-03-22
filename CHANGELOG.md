# Changelog

## 0.0.1
  * Fix arguments that ensure the compatibility to a relational target.

## 0.0.2
  * Fix getting a BrokenPipeError.

## 0.0.3
  * Fix syntax.

## 0.0.4
  * Fix syntax.

## 0.0.5
  * Fix getting BrokenPipeError when calling singer.write_state.

## 0.0.6
  * Remove handling BrokenPipeError, because this is the expected behaviour in some situations.

## 1.0.0
  * Inhacement: Add missing keys to rows and assing a default value ('').