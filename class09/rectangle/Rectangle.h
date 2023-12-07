#pragma once
#include<iostream>

class Rectangle {
private:
	float x;
	float y;
public:
	Rectangle() {
		x = 3.f;
		y = 4.f;
	}
	Rectangle(float x, float y) {
		this->x = x;
		this->y = y;
	}
	float get_area() {
		return x * y;
	}
};
